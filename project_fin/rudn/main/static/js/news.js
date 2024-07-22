
const NewsContainer = document.getElementsByClassName('news-block')
const InnerText = document.getElementById('InnerText')
const InnerTitle = document.getElementById('InnerTitle')
const InnreImg = document.getElementById('InnerImg')

for(i=0; i < NewsContainer.length; i++) {
    NewsContainer[i].addEventListener('click', function() {
        InnerText.innerText = this.childNodes[9].innerText
        InnerTitle.innerText = this.childNodes[1].innerText
        InnreImg.src = this.childNodes[5].src
    })
}
console.log(NewsContainer[3].childNodes)

