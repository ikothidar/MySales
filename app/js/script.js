$(document).ready(function () {
  const toggleButton = document.getElementById('toggle_button');
  const gstNumberContainer = document.getElementById('gst_number_container');
  const nameContainer = document.getElementById('name_container');

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
