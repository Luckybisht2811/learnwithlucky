// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 4. TYPING ANIMATION
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const words = ["Python", "Web Development", "Data Science", "DSA", "JavaScript"];
let wordIndex = 0, charIndex = 0, isDeleting = false;

function type() {
    const el = document.getElementById("typing-text");
    if (!el) return;
    const current = words[wordIndex];

    el.textContent = isDeleting
        ? current.substring(0, charIndex--)
        : current.substring(0, charIndex++);

    if (!isDeleting && charIndex === current.length + 1) {
        isDeleting = true;
        setTimeout(type, 1500);
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        setTimeout(type, 400);
    } else {
        setTimeout(type, isDeleting ? 60 : 100);
    }
}

document.addEventListener("DOMContentLoaded", type);