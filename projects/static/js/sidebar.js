$(window).ready(() => {
  if ($(window).outerWidth() <= 768) {
    $("#sidebar").removeClass("sidebar-container");
    $("#sidebar").addClass("sidebar-container-close");
  }
});

$("#close-sidebar").click(() => {
  $("#sidebar").removeClass("sidebar-container-open");
  $("#sidebar").animate({ width: "0" }, 500);
  $("#sidebar").addClass("sidebar-container-close");
});

$("#open-sidebar").click(() => {
  $("#sidebar").removeClass("sidebar-container-close");
  $("#sidebar").addClass("sidebar-container-open");
  $("#sidebar").animate({ width: "300px" }, 700);
});
