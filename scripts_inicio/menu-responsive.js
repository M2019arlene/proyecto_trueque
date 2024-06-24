const menuResponsive = document.querySelector(".menu-bar")
const iconBars = menuResponsive.querySelector('i');
const navigation = document.querySelector('.menu');

menuResponsive.addEventListener('click', () => {
    if(iconBars.classList.contains('fa-bars')){
        iconBars.classList.remove('fa-bars');
        iconBars.classList.add('fa-xmark');
    } else{
        iconBars.classList.remove("fa-xmark")
        iconBars.classList.add('fa-bars')
    }
    navigation.classList.toggle('navigation-responsive')
});