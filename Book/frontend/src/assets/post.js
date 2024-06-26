export function post(url = '', data = {}) {
    // 默认参数
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
        mode:"cors"
    };
    // 发送POST请求
    return fetch(url, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            throw error;
        });
}
