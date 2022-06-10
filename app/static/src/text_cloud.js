function getContentWidth (elem) {
  var element = document.getElementById(elem);
  var styles = getComputedStyle(element)

  return element.clientWidth
    - parseFloat(styles.paddingLeft)
    - parseFloat(styles.paddingRight)
}

function generate_text_cloud(elem, tagList){
    tagList = tagList;
    WordCloud(document.getElementById(elem), {
        list: tagList,
        gridSize: Math.round(16 * getContentWidth(elem) / 1024),
        rotateRatio: 0.5,
        drawOutOfBound: false
      });
};