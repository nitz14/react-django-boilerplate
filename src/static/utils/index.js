export function checkHttpStatus(response) {
    if (response.status >= 200 && response.status < 300) {
        return response;
    }

    const error = new Error(response.statusText);
    error.response = response;
    throw error;
}

export function parseJSON(response) {
    return response.json();
}

export function timeoutPromise(ms, promise) {
    const error = new Error('Timeout for request');
    error.response = 'Timeout';

    return new Promise((resolve, reject) => {
        const timeoutId = setTimeout(() => {
            reject(error);
        }, ms);
        promise.then(
            (res) => {
                clearTimeout(timeoutId);
                resolve(res);
            },
            (err) => {
                clearTimeout(timeoutId);
                reject(err);
            }
        );
    });
}
