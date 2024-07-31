document.addEventListener('DOMContentLoaded', function() {
    const dateElements = document.querySelectorAll('.datetime');
    dateElements.forEach(function(element) {
        const utcTimeStr = element.textContent.trim();
        const utcTime = new Date(utcTimeStr);
        const options = {
            year: 'numeric', month: 'long', day: 'numeric',
            hour: '2-digit', minute: '2-digit', second: '2-digit',
            hour12: false,
            timeZoneName: 'short'
        };
        const localTime = utcTime.toLocaleString('zh-TW', options);
        element.textContent = localTime;
    });
});