$(document).ready((event) => {
  $("#create_profile").submit((event) => {
    event.preventDefault();

    form = $("#create_profile");
    form_data = new FormData(this);

    $.ajax({
      url: "http://127.0.0.1:8000/api/profile/",
      type: "POST",
      data: form_data,
      dataType: "json",
      success: (data) => {
        alert(data["success"]);

        location.window.href = "/";
      },
    });

    $("#display_picture").val("");
    $("#user_bio").val("");
  });

  $("#new_project").submit((event) => {
    event.preventDefault();

    let form = $("#new_project");

    let form_data = new FormData();

    console.log($("#profile").val());

    form_data.append("title", $("#title").val());
    form_data.append("landing_page", $("#landing_page")[0].files[0]);
    form_data.append("link", $("#link").val());
    form_data.append("detailed_description", $("#description").val());
    form_data.append("profile", $("#profile").val());

    console.log(form_data);
    $.ajax({
      url: "http://127.0.0.1:8000/api/project/",
      type: "POST",
      cache: false,
      contentType: false,
      processData: false,
      dataType: "json",
      data: form_data,
      success: (data) => {
        alert(data["success"]);

        location.window.href = "/";
      },
      error: (error) => {
        console.log(error);
      },
    });

    $("#name").val("");
    $("#landing_image").val("");
    $("#link").val("");
    $("#description").val("");
  });
});
