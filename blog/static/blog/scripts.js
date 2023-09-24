let currentScrollPosition = 0;
let currentScrollAmount = 320;
const sCont = document.querySelector('story-container');
const hScroll = document.querySelector('.horizontal-scroll');

// SCROLL HANDLE
const btnScrollLeft = document.querySelector('#btn-scroll-left');
const btnScrollRight = document.querySelector('#btn-scroll-right');

btnScrollLeft.style.opacity = '0';

let maxScroll = -sCont.offsetWidth + hScroll.offsetWidth;

function csrollHorizontally(val) {
	currentScrollPosition += (val * currentScrollAmount);
	if (currentScrollPosition >=  0) {
		currentScrollPosition = 0;
		btnScrollLeft.style.opacity = "0";
	} else {
		btnScrollLeft.style.opacity = "1";
	}

	if (currentScrollPosition <=  maxScroll) {
		currentScrollPosition = maxScroll;
		btnScrollRight.style.opacity = "0";
	} else {
		btnScrollRight.style.opacity = "1";
	}

	sCont.style.left = currentScrollPosition + 'px';
} 