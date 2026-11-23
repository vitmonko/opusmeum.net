document.getElementById('year').textContent = new Date().getFullYear();

// "Copy email address" button: handy for people who write from webmail.
const copyButton = document.querySelector('.copy-email');
if (copyButton) {
  if (navigator.clipboard) {
    const label = copyButton.textContent;
    copyButton.addEventListener('click', () => {
      navigator.clipboard.writeText(copyButton.dataset.email).then(() => {
        copyButton.textContent = copyButton.dataset.done;
        setTimeout(() => { copyButton.textContent = label; }, 2500);
      });
    });
  } else {
    copyButton.hidden = true;
  }
}
