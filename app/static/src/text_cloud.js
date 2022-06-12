function getContentWidth (elem) {
  var element = document.getElementById(elem);
  var styles = getComputedStyle(element)

  return element.clientWidth
    - parseFloat(styles.paddingLeft)
    - parseFloat(styles.paddingRight)
}

function generate_text_cloud(elem, tagList, minFreq){
    console.log(minFreq)
    WordCloud(document.getElementById(elem), {
        list: tagList,
        weightFactor: (getContentWidth(elem)/214)*(6/minFreq),
        //gridSize: Math.round(16 * getContentWidth(elem) / 1024),
        //minSize: getContentWidth(elem)*0.0001,
        rotateRatio: 0.5,
        drawOutOfBound: false
      });
};