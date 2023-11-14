// Function to start the counter
function startCounter(maxValue, counterElement, speed = 1000000) {
    let count = 1;
    let magnitude = 1;
    const frameRate = 1000 / speed;  // Speed in frames per second

    const incrementCounter = () => {
        if (count <= maxValue) {
            counterElement.innerText = count;
            count += magnitude;
            if (count % 2 == 0) {
                magnitude++; // Magnitude ne kadar az sürede bir artarsa o kadar hızlı sayım olacak.
            }
            if(count < 20) {
                magnitude = 1;
                speed = speed / 10;
            }
            if ((maxValue - count) <= (count * 0.1)) {
                count = maxValue;
            }
            
            setTimeout(incrementCounter, frameRate);
        }
    }

    incrementCounter();
}


// Create an Intersection Observer for each counter
const counters = document.querySelectorAll(".counter");
counters.forEach(counterElement => {
    const maxValue = parseInt(counterElement.getAttribute("data-max"), 10);

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                startCounter(maxValue, counterElement);
                observer.unobserve(entry.target);
            }
        });
    });

    observer.observe(counterElement);
});

// Function to check if the user has scrolled more than 75%
function isScrolledPast75() {
    // Calculate the scroll position based on the document height
    const scrollPosition = (window.innerHeight + window.scrollY) / document.body.offsetHeight;
    return scrollPosition > 0.75;
}

// Function to load the Google Reviews script
function loadGoogleReviewsScript() {
    const script = document.createElement('script');
    script.src = 'https://widgets.sociablekit.com/google-reviews/widget.js';
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
}

// Event listener to check scroll position and load the script
window.addEventListener('scroll', function() {
    if (isScrolledPast75()) {
        loadGoogleReviewsScript();
        // Remove the event listener to prevent loading the script multiple times
        window.removeEventListener('scroll', arguments.callee);
    }
});
