// 01. Renderer Setting
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 02. Camera Setting
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
camera.position.set(0, 0, 100); // z축 방향으로 100만큼
camera.lookAt(0, 0, 0); // 원점을 바라보도록 설정

const scene = new THREE.Scene();

//create a blue LineBasicMaterial
const material = new THREE.LineBasicMaterial({color: 0x0000ff}); // 파란색 재질

// Define points
const points = [];
points.push(new THREE.Vector3(-10, 0, 0 ));
points.push(new THREE.Vector3(0, 10, 0 ));
points.push(new THREE.Vector3(10, 0, 0 ));

const geometry = new THREE.BufferGeometry().setFromPoints(points); // THREE.BufferGeometry()로 좌표 데이터 저장, setFromPoints(points)로 점을 연결

const line = new THREE.Line(geometry, material); // 파란색 선 생성

scene.add(line); // 씬에 선을 추가
renderer.render(scene, camera);