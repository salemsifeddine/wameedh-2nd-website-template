

function createProjectList() {
    let projects = [{
            header: "#1",
            author: "Web Application",
            title: "DSC RRU Website",
            text: "The website of Developer Student Club at Rashtriya Raksha University developed by the members of the club.",
            image: "imgs/projects/project1.png",
            goToLinkTitle: "Go to website",
            goToLink: "https://dsc-rsu.github.io/DSC-RRU-Website/",
        },
        {
            header: "#2",
            author: "Web Application",
            title: "Library Management System",
            text: "A Library Management System for RRU as a part of learning project while learning MERN Stack.",
            image: "imgs/projects/project2.jpg",
            goToLinkTitle: "Under Development",
            goToLink: "#",
        },
        {
            header: "#3",
            author: "Web Application",
            title: "Event Management System",
            text: "Book your seat at any events of RRU using this one-click event booking website. The participants can get access to thier certificates of the events.",
            image: "imgs/projects/project3.jpg",
            goToLinkTitle: "Under Development",
            goToLink: "#",
        },
    ];

    


function createNavBar(activePage) {
    

    $("#about-us").click((e) => {
        if ($("#home").hasClass("current-active"))
            $("#home").removeClass("current-active");
        $("#about-us").addClass("current-active");
    });

    if (window.location.hash.substr(1) === "abt-us") {
        if ($("#home").hasClass("current-active"))
            $("#home").removeClass("current-active");
        $("#about-us").addClass("current-active");
    }
}



function createPageHeader(title, subtitle, image, side = 0) {
    
    

    let margin = $(".header-nav").outerHeight();
    $(".project-header").css({
        "margin-top": margin,
        "height": "calc(100vh - " + margin + "px)"
    });
}


}
const phoneInputField = document.querySelector("#contactPhone");

