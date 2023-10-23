if (document.body.style.filter === 'invert(1) hue-rotate(180deg)') {
    document.body.style.filter = '';
  } else {
    document.body.style.filter = 'invert(1) hue-rotate(180deg)';
  }
  
  let images = document.querySelectorAll('img');
  images.forEach(img => {
      img.style.filter = 'invert(1) hue-rotate(180deg)'; 
  });