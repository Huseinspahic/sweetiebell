document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initAnimations();
    
    // Mobile menu handling
    initMobileMenu();
    
    // Handle form validation
    initFormValidation();
});

/**
 * Initialize fade-in animations
 */
function initAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');
    
    // Show elements that are already in view on page load
    checkFadeElements();
    
    // Check elements on scroll
    window.addEventListener('scroll', checkFadeElements);
    
    function checkFadeElements() {
        fadeElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 100) {
                element.classList.add('visible');
            }
        });
    }
}

/**
 * Initialize mobile menu handling
 */
function initMobileMenu() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        // Close mobile menu when clicking a link
        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }
}

/**
 * Initialize form validation
 */
function initFormValidation() {
    const orderForm = document.getElementById('orderForm');
    
    if (orderForm) {
        orderForm.addEventListener('submit', function(event) {
            if (!orderForm.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            orderForm.classList.add('was-validated');
        });
    }
}

/**
 * Set minimum date for order date input to today
 */
function setMinDate() {
    const dateInput = document.getElementById('date');
    if (dateInput) {
        const today = new Date();
        const yyyy = today.getFullYear();
        let mm = today.getMonth() + 1;
        let dd = today.getDate();
        
        if (dd < 10) dd = '0' + dd;
        if (mm < 10) mm = '0' + mm;
        
        const formattedToday = yyyy + '-' + mm + '-' + dd;
        dateInput.setAttribute('min', formattedToday);
    }
}

/**
 * Calculate the product total price based on quantity
 */
function updateTotal() {
    const productSelect = document.getElementById('product');
    const quantityInput = document.getElementById('quantity');
    const totalDisplay = document.getElementById('totalDisplay');
    
    if (productSelect && quantityInput && totalDisplay) {
        const selectedOption = productSelect.options[productSelect.selectedIndex];
        const price = parseFloat(selectedOption.dataset.price || 0);
        const quantity = parseInt(quantityInput.value) || 0;
        const total = (price * quantity).toFixed(2);
        
        totalDisplay.textContent = `$${total}`;
    }
}

// When the page finishes loading
window.addEventListener('load', function() {
    setMinDate();
    
    // Initialize total price calculation if on order page
    const productSelect = document.getElementById('product');
    const quantityInput = document.getElementById('quantity');
    
    if (productSelect && quantityInput) {
        productSelect.addEventListener('change', updateTotal);
        quantityInput.addEventListener('input', updateTotal);
        updateTotal(); // Initial calculation
    }
});
