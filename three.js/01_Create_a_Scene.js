const scene = new THREE.Scene(); // Generate 3D scene
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000); // 시야각 75도, 가로 세로 비율, 최소 거리, 최대 거리

const renderer = new THREE.WebGLRenderer(); // Rendering 3D Object
renderer.setSize(window.innerWidth, window.innerHeight); // Display Size (Browser)
renderer.setAnimationLoop(animate); // animate function을 every frame마다 호출되도록 설정 (지속적인 갱신)
document.body.appendChild(renderer.domElement); // 실제 렌더링된 화면을 담고 있는 HTML 요소를 <body>에 추가하여 화면에 3D graphic 표시

const geometry = new THREE.BoxGeometry(1, 1, 1); // 1x1x1 크기의 큐브 모양의 기하학적 객체
const material = new THREE.MeshBasicMaterial({color: 0x00ff00}); // 초록색 재질
const cube = new THREE.Mesh(geometry, material); // 초록색 3D 큐브 생성
scene.add(cube); // 씬에 큐브를 추가

camera.position.z = 5; // 기본적으로 카메라는 원점(0, 0, 0)에서 바라보므로, 카메라를 z축 방향으로 5만큼 이동 

function animate() { // 큐브를 회전시키고 렌더링하는 역할
	cube.rotation.x += 0.01; // 큐브를 x축을 기준으로 1프레임마다 0.01만큼 회전
	cube.rotation.y += 0.01; // 큐브를 y축을 기준으로 1프레임마다 0.01만큼 회전

	renderer.render(scene, camera); // 씬을 화면에 표시
}