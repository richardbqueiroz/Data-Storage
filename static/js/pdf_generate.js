function generatePDF() {
    const pdfWindow = window.open(window.location.href + '?format=pdf', '_blank');
    pdfWindow.focus();
}