/* navbar.js — shared navbar for all pages */
document.addEventListener('DOMContentLoaded', function() {
  const navbar = `
  <nav>
    <div class="nav-inner">
      <a class="nav-logo" href="index.html">⚡ AI HUB</a>
      <div class="nav-links">
        <a href="index.html">Home</a>
        <div class="dropdown">
          <button class="dropdown-btn">AI Categories ▾</button>
          <div class="dropdown-menu">
            <a href="cat-text.html">✍️ Text &amp; Writing</a>
            <a href="cat-image.html">🎨 Image Generation</a>
            <a href="cat-video.html">🎬 Video Creation</a>
            <a href="cat-audio.html">🎵 Audio &amp; Music</a>
            <a href="cat-code.html">💻 Coding &amp; Dev</a>
            <a href="cat-chat.html">💬 Chatbots &amp; LLMs</a>
            <a href="cat-research.html">🔬 Research &amp; Data</a>
            <a href="cat-design.html">🖌️ Design &amp; UI</a>
            <a href="cat-business.html">📊 Business &amp; Marketing</a>
            <a href="cat-productivity.html">⚡ Productivity</a>
          </div>
        </div>
        <a href="about.html">About Us</a>
        <a href="contact.html">Contact</a>
      </div>
    </div>
  </nav>`;
  document.body.insertAdjacentHTML('afterbegin', navbar);

  /* Highlight active nav link */
  const page = window.location.pathname.split('/').pop();
  document.querySelectorAll('.nav-links > a').forEach(a => {
    if (a.getAttribute('href') === page) a.classList.add('active');
  });
});
