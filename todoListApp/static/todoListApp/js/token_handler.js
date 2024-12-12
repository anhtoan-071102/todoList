class TokenHandler {
    static setTokens(access, refresh) {
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);
        localStorage.setItem('token_timestamp', Date.now().toString());
    }

    static getAccessToken() {
        return localStorage.getItem('access_token');
    }

    static getRefreshToken() {
        return localStorage.getItem('refresh_token');
    }

    static removeTokens() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('token_timestamp');
    }

    static async refreshAccessToken() {
        try {
            const response = await fetch('/api/token/refresh/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    refresh: this.getRefreshToken()
                })
            });

            if (!response.ok) {
                throw new Error('Token refresh failed');
            }

            const data = await response.json();
            this.setTokens(data.access, this.getRefreshToken());
            return data.access;
        } catch (error) {
            this.removeTokens();
            window.location.href = '/api/login-page/';
            throw error;
        }
    }

    static async fetchWithToken(url, options = {}) {
        let token = this.getAccessToken();
        
        options.headers = {
            ...options.headers,
            'Authorization': `Bearer ${token}`
        };

        try {
            let response = await fetch(url, options);

            if (response.status === 401) {
                token = await this.refreshAccessToken();
                options.headers['Authorization'] = `Bearer ${token}`;
                response = await fetch(url, options);
            }

            return response;
        } catch (error) {
            console.error('Fetch error:', error);
            throw error;
        }
    }
}