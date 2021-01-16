function renderLeftIndexList() {
	let leftImgs = imgs.filter((img) => {
		return imgs.indexOf(img) <= Math.ceil(imgs.length / 3 - 1);
	});
	return generateIndexListHTML(leftImgs);
}

function renderMiddleIndexList() {
	let middleImgs = imgs.filter((img) => {
		return (
			imgs.indexOf(img) > Math.ceil(imgs.length / 3 - 1) &&
			imgs.indexOf(img) <= Math.ceil((imgs.length * 2) / 3 - 1)
		);
	});
	return generateIndexListHTML(middleImgs);
}

function renderRightIndexList() {
	let rightImgs = imgs.filter((img) => {
		return imgs.indexOf(img) > Math.ceil((imgs.length * 2) / 3 - 1);
	});
	return generateIndexListHTML(rightImgs);
}

function determineIndexToggle(navLink) {
	if (
		($(navLink).hasClass("secondary") || $(navLink).hasClass("vid-link")) &&
		!$("#index-btn").hasClass("hidden")
	) {
		toggleIndex(true);
	} else if (
		!$(navLink).hasClass("secondary") &&
		!$(navLink).hasClass("vid-link") &&
		$("#index-btn").hasClass("hidden")
	) {
		toggleIndex(false);
	}
}

function createIndexLinkListeners() {
	$(".index-link").on("click", async function (evt) {
		evt.preventDefault();
		$("#img-container").empty();
		let filename = $(this).attr("id");
		for (let img of imgs) {
			if (img.filename === filename) {
				currentImgIndex = imgs.indexOf(img);
				break;
			}
		}
		const resp = await axios.get(`http://127.0.0.1:5000/img/${filename}`);
		img = resp.data.img;
		const imgHTML = generateImgHTML(img.filename, currentPage, img.description);
		fadeImg(imgHTML);
	});
}

function toggleIndex(shouldBeHidden) {
	if (shouldBeHidden === true) {
		$("#index-btn").addClass("hidden");
		indexIsHidden = true;
	} else {
		$("#index-btn").removeClass("hidden");
		indexIsHidden = false;
	}
}

function generateIndexListHTML(imgs) {
	let listItems = "";
	for (let img in imgs) {
		listItems += `
        <li>
            <div class="row justify-content-center thumbnail-div my-2">
                <a id="${imgs[img].filename}" class="index-link" href="">
                    <img class="thumbnail" src="https://ncgbucket.s3.amazonaws.com/images/${currentPage}/${imgs[img].filename}" />
                </a>
            <div>
        </li>`;
	}
	return listItems;
}
