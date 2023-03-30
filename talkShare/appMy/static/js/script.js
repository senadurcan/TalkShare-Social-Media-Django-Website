// SIDEBAR
const menuItems = document.querySelectorAll('.menu-item');

// THEME
const theme = document.querySelectorAll('#theme');
const themeModal = document.querySelectorAll('.customize-theme');
const fontSizes = document.querySelectorAll('.choose-size span');


// -----SIDEBAR-----

//aktif olanları kaldırma

const changeActiveItem = () => {
    menuItems.forEach(item => {
        item.classList.remove('active');
    })
}

menuItems.forEach(item => {
    item.addEventListener('click',() => {
        changeActiveItem();
        item.classList.add('active');
    })
})


// -----THEME-----

// opens
const openThemeModal = () =>{
    themeModal.style.display = 'grid';
}

// close
const closeThemeModal = (e) => {
    if(e.target.classList.contains('customize-theme')){
        themeModal.style.display = 'none';
    }
}
themeModal.addEventListener('click', closeThemeModal);

theme.addEventListener('click', openThemeModal);

// -----FONTS-----
fontSizes.forEach(size=>{
    let fontSize;
    if(size.classList.contains('font-size-1')){
        fontSize = '10px';
    } else if (size.classList.contains('font-size-2')){
        fontSize = '13px';
    }else if (size.classList.contains('font-size-3')){
        fontSize = '16px';
    }else if (size.classList.contains('font-size-4')){
        fontSize = '19px';
    }else if (size.classList.contains('font-size-5')){
        fontSize = '22px';
    }
})

/* global bootstrap: false */
(() => {
    'use strict'
    const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(tooltipTriggerEl => {
      new bootstrap.Tooltip(tooltipTriggerEl)
    })
  })()
  