$(document).ready(function () {
	/* Check width on page load*/
	if ($(window).width() < 992) {
		$("#index-sidebar").removeClass("scroll");
		$("#fwd-btn").addClass("mobile");
		$("#back-btn").addClass("mobile");
		$("#main-row-wrapper").addClass("mobile");
		$("#main-row").removeClass("row");
		$("#main-row").addClass("col");
		$("#main-row").addClass("px-0");
	} else {
		$("#index-sidebar").addClass("scroll");
		$("#fwd-btn").removeClass("mobile");
		$("#back-btn").removeClass("mobile");
		$("#main-row-wrapper").removeClass("mobile");
		$("#main-row").removeClass("col");
		$("#main-row").removeClass("px-0");
		$("#main-row").addClass("row");
	}
});

$(window).resize(function () {
	/*If browser resized, check width again */
	if ($(window).width() < 992) {
		$("#index-sidebar").removeClass("scroll");
		$("#fwd-btn").addClass("mobile");
		$("#back-btn").addClass("mobile");
		$("#main-row-wrapper").addClass("mobile");
		$("#main-row").removeClass("row");
		$("#main-row").addClass("col");
		$("#main-row").addClass("px-0");
	} else {
		$("#index-sidebar").addClass("scroll");
		$("#fwd-btn").removeClass("mobile");
		$("#back-btn").removeClass("mobile");
		$("#main-row-wrapper").removeClass("mobile");
		$("#main-row").removeClass("col");
		$("#main-row").removeClass("px-0");
		$("#main-row").addClass("row");
	}
});

function handleImagesLink(resp) {
	imgs = resp.data.imgs;
	const firstImgHTML = generateImgHTML(
		imgs[currentImgIndex].filename,
		currentPage,
		imgs[currentImgIndex].description
	);

	const leftIndexListHTML = renderLeftIndexList();
	const middleIndexListHTML = renderMiddleIndexList();
	const rightIndexListHTML = renderRightIndexList();
	$("#img-container").append(firstImgHTML);
	$("#index-list-left").append(leftIndexListHTML);
	$("#index-list-middle").append(middleIndexListHTML);
	$("#index-list-right").append(rightIndexListHTML);
	createIndexLinkListeners();
}

function generateImgHTML(filename, folder, description) {
	if (description) {
		return `
			<img id="main-img" src="../static/images/${folder}/${filename}" />
			<p class="img-description">${description}</p>
		`;
	}
	return `<img id="main-img" src="../static/images/${folder}/${filename}" />`;
}

function getNextOrPrevImg() {
	const soughtImgHTML = generateImgHTML(
		imgs[currentImgIndex].filename,
		currentPage,
		imgs[currentImgIndex].description
	);
	fadeImg(soughtImgHTML);
}

function fadeImg(imgHTML) {
	$("#img-container").fadeOut(250);
	setTimeout(() => {
		$("#img-container").empty();
		$("#img-container").append(imgHTML);
	}, 250);
	$("#img-container").fadeIn(250);
}

$("#fwd-btn").on("click", () => {
	if (currentImgIndex === imgs.length - 1) {
		currentImgIndex = 0;
	} else {
		currentImgIndex++;
	}
	getNextOrPrevImg();
});

$("#back-btn").on("click", () => {
	if (currentImgIndex === 0) {
		currentImgIndex = imgs.length - 1;
	} else {
		currentImgIndex--;
	}
	getNextOrPrevImg();
});
