$(document).ready(function () {
  const toggleButton = document.getElementById('has_gst');
  const gstNumberContainer = document.getElementById('gst_number');
  const nameContainer = document.getElementById('party_name');

  function gstContianerVisiblity() {
    if (toggleButton.checked) {
      gstNumberContainer.hidden = false;
      nameContainer.hidden = true;
    } else {
      gstNumberContainer.hidden = true;
      nameContainer.hidden = false;
    }
  }

  // for first time when page will be loaded
  gstContianerVisiblity()

  // for tracking changes in switch
  toggleButton.addEventListener('change', () => {
    gstContianerVisiblity()
  });
});
