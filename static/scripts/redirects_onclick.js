function redirect_to(url) {
    window.location.href = url;
}

document.getElementById('device-a-state').addEventListener('click', () => {
    redirect_to("/app/device-a/state")
});

document.getElementById('device-b-state').addEventListener('click', (e) => {
    redirect_to("/app/device-b/state")
});

document.getElementById('block-c-state').addEventListener('click', (e) => {
    redirect_to("/app/block-c/state")
});

document.getElementById('device-b-frames-sender').addEventListener('click', (e) => {
    redirect_to("/app/device-b/frames-sender")
});

document.getElementById('app-edit-config').addEventListener('click', (e) => {
    redirect_to("/app/edit-config")
});
