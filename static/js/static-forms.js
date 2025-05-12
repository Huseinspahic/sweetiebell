/**
 * Handles form submissions for static site deployment
 */
document.addEventListener('DOMContentLoaded', function() {
    // Initialize order form handler
    initOrderForm();
    
    // Initialize contact form handler
    initContactForm();
});

/**
 * Initialize order form handling
 */
function initOrderForm() {
    const orderForm = document.getElementById('orderForm');
    
    if (orderForm) {
        orderForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            if (!orderForm.checkValidity()) {
                event.stopPropagation();
                orderForm.classList.add('was-validated');
                return;
            }
            
            // Collect form data
            const formData = new FormData(orderForm);
            const formObject = {};
            formData.forEach((value, key) => formObject[key] = value);
            
            // You would normally send this data to a server
            // For a static site, we'll use a third-party form service
            // This is a placeholder - replace with actual service
            
            // Show success message
            const formContainer = document.querySelector('.order-form');
            formContainer.innerHTML = `
                <div class="text-center py-5">
                    <i class="fas fa-check-circle text-success" style="font-size: 4rem;"></i>
                    <h2 class="mt-4">Thank You!</h2>
                    <p class="lead">Your order has been submitted successfully.</p>
                    <p>We will contact you shortly to confirm your order details.</p>
                    <a href="./index.html" class="btn btn-primary mt-3">Return to Home</a>
                </div>
            `;
            
            // Log the order for demo purposes
            console.log('Order submitted:', formObject);
        });
    }
}

/**
 * Initialize contact form handling
 */
function initContactForm() {
    const contactForm = document.querySelector('form');
    
    if (contactForm && contactForm.querySelector('#contactName')) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            if (!contactForm.checkValidity()) {
                event.stopPropagation();
                contactForm.classList.add('was-validated');
                return;
            }
            
            // Collect form data
            const formData = new FormData(contactForm);
            const formObject = {};
            formData.forEach((value, key) => formObject[key] = value);
            
            // You would normally send this data to a server
            // For a static site, we'll use a third-party form service
            // This is a placeholder - replace with actual service
            
            // Show success message
            contactForm.innerHTML = `
                <div class="text-center py-3">
                    <i class="fas fa-check-circle text-success" style="font-size: 3rem;"></i>
                    <h3 class="mt-3">Message Sent!</h3>
                    <p>Thank you for reaching out. We'll be in touch soon!</p>
                </div>
            `;
            
            // Log the message for demo purposes
            console.log('Contact message submitted:', formObject);
        });
    }
}

/**
 * Load products from JSON file (for static site)
 */
async function loadProductsData() {
    try {
        const response = await fetch('./static/products.json');
        if (!response.ok) {
            throw new Error('Failed to load products data');
        }
        return await response.json();
    } catch (error) {
        console.error('Error loading products:', error);
        return { cakes: [], muffins: [], desserts: [], all_products: [] };
    }
}