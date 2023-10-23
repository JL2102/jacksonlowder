document.getElementById('toggleDarkMode').addEventListener('click', () => {
    chrome.tabs.executeScript({
      file: 'content.js'
    });
  });
  