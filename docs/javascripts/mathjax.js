window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"], ["$", "$"]],
        displayMath: [["\\[", "\\]"], ["$$", "$$"]],
        processEscapes: true,
        processEnvironments: true
    }
};

document.addEventListener("DOMContentLoaded", function () {
    MathJax.typesetPromise();
});
