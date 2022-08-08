const activeToolEl = document.getElementById('active-tool');
const bucketColorBtn = document.getElementById('paint-tool');
const clearCanvasBtn = document.getElementById('clear-tool');
const downloadBtn = document.getElementById('download-tool');

const brushColorBtn = document.getElementById('brush-color');
// const brushIcon = document.getElementById('brush');
const brushSize = document.getElementById('brush-size');
const brushSlider = document.getElementById('brush-slider');
const eraser = document.getElementById('eraser-tool');

const saveStorageBtn = document.getElementById('save-storage');
const loadStorageBtn = document.getElementById('load-storage');
const clearStorageBtn = document.getElementById('clear-storage');

// const postBtn = document.getElementById('post-tool');

const { body } = document;
const BRUSH_TIME = 1500;

// Global Variables
// const canvas = document.createElement('canvas');
const canvas = document.getElementById('canvas')
canvas.id = 'canvas';
const context = canvas.getContext('2d');

let currentSize = 10;
let bucketColor = '#FFFFFF';
let currentColor = '#2638AB';
let isEraser = false;
let isMouseDown = false;
let drawnArray = [];

// Formatting Brush Size
function displayBrushSize() {
  if (brushSlider.value < 10) brushSize.textContent = `0${brushSlider.value}`;
  else brushSize.textContent = brushSlider.value;
}

// Setting Brush Size
brushSlider.addEventListener('change', () => {
  currentSize = brushSlider.value;
  displayBrushSize();
  activeToolEl.textContent = 'Brush Size Changed';
});

// Setting Brush Color
brushColorBtn.addEventListener('change', () => {//브러시 색상을 선택하면
  isEraser = false; //지우개가 아니라 브러시가 선택되고
  currentColor = `#${brushColorBtn.value}`; //방금 선택한 색상이 브러시 색상으로 지정됨
  activeToolEl.textContent = 'Brush Color Changed';
});


// Setting Background Color
bucketColorBtn.addEventListener('change', () => {
  bucketColor = `#${bucketColorBtn.value}`;
  context.fillStyle = bucketColor;
  context.fillRect(0, 0, canvas.width, canvas.height);
  // clearCanvas();
  restoreCanvas();
  activeToolEl.textContent = 'Background Color Changed';
});


// Eraser
eraser.addEventListener('click', () => { //지우개 버튼을 클릭하면
  isEraser = true; //브러시가 아니라 지우개가 선택되고
  currentColor = `#${bucketColorBtn.value}`; //현재 색상이 배경색으로 변경됨
  currentSize = 50; //자우개 사이즈는 50으로 설정됨
  activeToolEl.textContent = 'Eraser'; 
});


// Switch back to Brush
function switchToBrush() {
  isEraser = false; //지우개가 아니라고 표시
  activeToolEl.textContent = 'Brush';
  currentColor = `#${brushColorBtn.value}`; //현재 색상이 브러시 색으로 변경됨
  currentSize = 10; //현재 사이즈 10으로 변경됨
  brushSlider.value = 10; //브러시 슬라이더의 값도 당연히 10으로 맞춰짐.
  displayBrushSize();
}


function brushTimeSetTimeout(ms) {
  setTimeout(switchToBrush, ms); //switchToBrush 호출을 ms시간 만큼 미룸
}


// Canvas
function clearCanvas() {
  canvas.width = 2000;
  canvas.height = 2000;
  context.fillStyle = '#FFFFFF';
  context.fillRect(0, 0, canvas.width, canvas.height);
  activeToolEl.textContent = 'Not painted yet';
  switchToBrush();
}

// Clear Canvas
clearCanvasBtn.addEventListener('click', () => {
  clearCanvas();
  drawnArray = [];
  //Active Tool
  activeToolEl.textContent = 'Canvas Reset';
  brushTimeSetTimeout(BRUSH_TIME);
});



// Draw what is stored in DrawnArray
function restoreCanvas() {
  for (let i = 1; i < drawnArray.length; i++) {
    context.beginPath(); //선 그리기 시작
    context.moveTo(drawnArray[i - 1].x, drawnArray[i - 1].y); //이전에 찍은 데로 이동함(선은 그려지지 X)
    context.lineWidth = drawnArray[i].size; //길이는 size에 저장된 값만큼
    context.lineCap = 'round'; //선끝모양은 round
    if (drawnArray[i].eraser) { //만약 이번 게 eraser=True이었다면
      context.strokeStyle = bucketColorBtn.value; //(색깔이 배경색으로 바뀌어야 하니까bucketColor로 돌려놓기
    } else { //eraser=False 라면, 즉 브러시라면
      context.strokeStyle = drawnArray[i].color; //이번 drawnArray 요소에 저장된 색상으로 지정
    }
    context.lineTo(drawnArray[i].x, drawnArray[i].y); //이번 x,y좌표까지 경로을 그림
    context.stroke(); //경로에 따라 선을 그림
  }
}

// Store Drawn Lines in DrawnArray
function storeDrawn(x, y, size, color, erase) {
  const line = {
    x,
    y,
    size,
    color,
    erase,
  };
  // console.log(line);
  drawnArray.push(line);
}



// Get Mouse Position
function getMousePosition(event) {
  const boundaries = canvas.getBoundingClientRect();
  return {
    x: event.clientX - boundaries.left,
    y: event.clientY - boundaries.top,
  };
}

// Mouse Down: 마우스 왼쪽버튼 누르고 있을 때 발생
canvas.addEventListener('mousedown', (event) => { 
  isMouseDown = true;
  const currentPosition = getMousePosition(event);
  context.moveTo(currentPosition.x, currentPosition.y);
  context.beginPath();
  context.lineWidth = currentSize;
  context.lineCap = 'round';
  context.strokeStyle = currentColor;
});

// Mouse Move
canvas.addEventListener('mousemove', (event) => {
  if (isMouseDown) {
    const currentPosition = getMousePosition(event);
    context.lineTo(currentPosition.x, currentPosition.y);
    context.stroke();
    storeDrawn(
      currentPosition.x,
      currentPosition.y,
      currentSize,
      currentColor,
      isEraser,
    );
  } else {
    storeDrawn(undefined);
  }
});

// Mouse Up: 마우스 왼쪽버튼 누르고 있다가 뗄 때 발생
canvas.addEventListener('mouseup', () => {
  isMouseDown = false;
});



// Save to Local Storage
saveStorageBtn.addEventListener('click', () => {
  localStorage.setItem('savedCanvas', JSON.stringify(drawnArray));
  // Active Tool
  activeToolEl.textContent = 'Canvas Saved';
  brushTimeSetTimeout(BRUSH_TIME);
});

// Load from Local Storage
loadStorageBtn.addEventListener('click', () => {
  if (localStorage.getItem('savedCanvas')) {

    context.fillStyle = `#${bucketColorBtn.value}`
    context.fillRect(0, 0, canvas.width, canvas.height);
    
    drawnArray = JSON.parse(localStorage.savedCanvas);
    restoreCanvas();
    // Active Tool
    activeToolEl.textContent = 'Canvas Loaded';
    brushTimeSetTimeout(BRUSH_TIME);
  } else {
    activeToolEl.textContent = 'No Canvas Found';
    brushTimeSetTimeout(BRUSH_TIME);
  }
});

// Clear Local Storage
clearStorageBtn.addEventListener('click', () => {
  localStorage.removeItem('savedCanvas');
  // Active Tool
  activeToolEl.textContent = 'Local Storage Cleared';
  brushTimeSetTimeout(BRUSH_TIME);
});

// Download Image
downloadBtn.addEventListener('click', () => {
  downloadBtn.href = canvas.toDataURL('image/jpeg', 1);
  downloadBtn.download = 'diary.jpg';
  // Active Tool
  activeToolEl.textContent = 'Image File Saved';
  brushTimeSetTimeout(BRUSH_TIME);
});


// On Load
clearCanvas();
