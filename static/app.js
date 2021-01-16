var currentPage;
var imgs;
var currentImgIndex;
var indexIsHidden = true;

$(".nav-link").on("click", async function (evt) {
	evt.preventDefault();
	$(".nav-link").removeClass("font-weight-bold");
	$(".nav-link").removeClass("large-text");
	$(this).addClass("font-weight-bold");
	$(this).addClass("large-text");
	$("#index-list-left").empty();
	$("#index-list-middle").empty();
	$("#index-list-right").empty();

	if ($(".collapse").hasClass("show")) {
		$(".collapse").removeClass("show");
	}

	determineIndexToggle(this);
	determineScrollBtnToggle(this);

	$("#img-container").empty();

	currentPage = $(this).attr("id");
	currentImgIndex = 0;
	const resp = await axios.get(`http://127.0.0.1:5000/${currentPage}`);
	if (resp.data.imgs) {
		handleImagesLink(resp);
	} else if (resp.data.vids) {
		handleVideosLink(resp);
	} else {
		handleSecondaryLink(resp);
	}
});

function handleSecondaryLink(resp) {
	const contactInfo = resp.data.info;
	let contactHTML = generateContactHTML(contactInfo);
	$("#img-container").append(contactHTML);
}

function determineScrollBtnToggle(navLink) {
	if (
		!$("#scroll-btn").hasClass("hidden") &&
		($(navLink).hasClass("secondary") || $(navLink).hasClass("vid-link"))
	) {
		toggleScrollBtn(true);
	} else if (
		$("#scroll-btn").hasClass("hidden") &&
		!$(navLink).hasClass("secondary") &&
		!$(navLink).hasClass("vid-link")
	) {
		toggleScrollBtn(false);
	}
}

function toggleScrollBtn(shouldBeHidden) {
	if (shouldBeHidden === true) {
		$("#scroll-btn").addClass("hidden");
		indexIsHidden = true;
	} else {
		$("#scroll-btn").removeClass("hidden");
		indexIsHidden = false;
	}
}

function generateContactHTML(info) {
	return `<div class="col-12 ml-lg-5 pl-lg-4 mt-3">
        <div class="row justify-content-start mb-3">
            <b>Contact</b>
        </div>
        <div class="row justify-content-start">
            <ul id="contact-info-list" class="px-0">
                <li>Email: <a href="mailto: ${info.email}">${info.email}</a></li>
                <li>Instagram: <a href="${info.instagram}">@dracaenaamericana</a></li>
				<li>IMDB: <a href="${info.imdb}">${info.imdb}</a></li>
				<li>Old Website: <a href="${info.website}">${info.website}</a></li>
			</ul>
		</div>
		<div class="row justify-content-start">
			<img id="prof-pic" class="col-12 col-lg-6 p-0 mr-0 mt-5" src="https://ncgbucket.s3.amazonaws.com/images/contact_imgs/nickgriffo.jpg">
		</div>
	</div>`;
}
