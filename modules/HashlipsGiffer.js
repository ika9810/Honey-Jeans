const GifEncoder = require("gif-encoder-2");
const { writeFile } = require("fs");

class HashLipsGiffer {
  constructor(_canvas, _ctx, _fileName, _repeat, _quality, _delay) {
    this.canvas = _canvas;
    this.ctx = _ctx;
    this.fileName = _fileName;
    this.repeat = _repeat;
    this.quality = _quality;
    this.delay = _delay;
    this.initGifEncoder();
  }

  initGifEncoder() {	
  //initGifEncoder = () => {
    this.gifEncoder = new GifEncoder(this.canvas.width, this.canvas.height);
    this.gifEncoder.setQuality(this.quality);
    this.gifEncoder.setRepeat(this.repeat);
    this.gifEncoder.setDelay(this.delay);
  };
  start() {
  //start = () => {
    this.gifEncoder.start();
  };
  add() {
  //add = () => {
    this.gifEncoder.addFrame(this.ctx);
  };
  stop() {
  //stop = () => {
    this.gifEncoder.finish();
    const buffer = this.gifEncoder.out.getData();
    writeFile(this.fileName, buffer, (error) => {});
    console.log(`Created gif at ${this.fileName}`);
  };
}

module.exports = HashLipsGiffer;
