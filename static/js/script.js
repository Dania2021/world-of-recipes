// Using setTimeout to automatically dismiss messages adapted from Code Institute Django Blog tutorial
try {
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
} catch (err) {
    console.info(err.toString());
}