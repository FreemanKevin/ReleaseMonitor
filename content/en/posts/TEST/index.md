---
title: "Elasticsearch Releases"
date: 2024-07-31
---

<div id="releases"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    fetch('https://github.com/FreemanKevin/ReleaseMonitor/raw/main/data/elasticsearch_releases.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('releases');
        data.forEach(release => {
            const date = new Date(release.published_at);
            const localDate = date.toLocaleString();
            container.innerHTML += `<p>Version: ${release.tag_name} - Published At: ${localDate}</p>`;
        });
    })
    .catch(error => console.error('Error loading the data:', error));
});
</script>