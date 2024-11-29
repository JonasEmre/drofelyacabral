// Sayaç fonksiyonu
function startCounter(maxValue, counterElement, speed = 100) {
    let count = 1;
    let magnitude = 1;
    const frameRate = 1000 / speed;  // Hız

    const incrementCounter = () => {
        if (count <= maxValue) {
            counterElement.innerText = count;
            count += magnitude;
            if (count % 2 === 0) {
                magnitude++; // Magnitude ne kadar az sürede bir artarsa o kadar hızlı sayım olacak.
            }
            if (count < 20) {
                magnitude = 1;
                speed = speed / 10;
            }
            if ((maxValue - count) <= (count * 0.1)) {
                count = maxValue;
            }

            setTimeout(incrementCounter, frameRate);
        }
    };

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
