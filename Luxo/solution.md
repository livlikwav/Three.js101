# 과제 1 : Implementing Luxo

const room = {width:30, height:20};
const cubeGeo = new THREE.BoxBufferGeometry(room.width, room.height, room.width); // 30, 20, 30
const baseMesh = {width:4, height:1, color:'red'};
const baseDiscMesh = {radius: 1, height: 0.2, color:'orange', segs:8};
new THREE.CylinderBufferGeometry
baseMesh.mesh.scale.set(baseMesh.width, baseMesh.height, baseMesh.width);

방
mesh.position.set(0, room.height / 2, 0); // 0, 10, 0
카메라
camera.position.set(0, room.height*0.5, room.width*1.4);
포인트 빛
light.position.set(0, room.height, 0);

baseMesh height = 1
그럼 0.5씩
bashDiscMesh height = 0.2


base.position.y = baseMesh.height/2;
baseDisc.position.y = baseMesh.height/2;
baseDiscMesh.mesh.position.y = baseDiscMesh.height/2;

base (0, 0.5, 0)
baseDisc(0, 0.5, 0)
baseDiscMesh(0, 0.25, 0)
근데!!! 
baseDiscMesh는 baseDisc라는 localspace상의 위치이므로
전체 위치상에서는 0.75임

