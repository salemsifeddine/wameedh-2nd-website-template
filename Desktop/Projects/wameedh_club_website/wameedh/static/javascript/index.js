import * as THREE from "three";
import { Earth } from "{% static  'javascript/earth' %}";
import { Moon } from "{% static  'javascript/moon' %}";
import { TrackballControls } from "three/examples/jsm/controls/TrackballControls";
import { WebGLRenderer } from 'three/src/renderers/WebGLRenderer';

addEventListener("DOMContentLoaded", () => {
  new HeyMoon();
});

export default class HeyMoon {

  constructor() {

    // シーン作成
    this.scene = new THREE.Scene();

    // カメラ作成
    this.camera = new THREE.PerspectiveCamera(
      60,
      innerWidth / innerHeight,
      1, 2000
    );
    this.camera.position.set(300, 35, 100);
    this.camera.lookAt(new THREE.Vector3(0, 0, 0));

    // レンダラー作成
    this.renderer = new WebGLRenderer({
      antialias: devicePixelRatio === 1,
    });
    this.renderer.setSize(innerWidth, innerHeight);
    this.renderer.setPixelRatio(devicePixelRatio);
    this.renderer.setClearColor(0x000000, 1);
    this.renderer.shadowMap.enabled = true;

    const container = document.getElementById("canvas-container");
    container.appendChild(this.renderer.domElement);

    // カメラコントローラー追加
    this.controller = new TrackballControls(
      this.camera,
      this.renderer.domElement
    );
    this.controller.noPan = true;
    this.controller.minDistance = 200;
    this.controller.maxDistance = 1000;
    this.controller.dynamicDampingFactor = 0.05;

    // 環境光作成
    const ambientLight = new THREE.AmbientLight(0x111111);
    this.scene.add(ambientLight);

    // スポットライト作成
    const spotLight = new THREE.SpotLight(0xffffff);
    spotLight.position.set(1000, 0, 0);
    spotLight.castShadow = true;
    this.scene.add(spotLight);

    // 地球読み込み
    this.earth = new Earth();
    this.scene.add(this.earth);

    // 月読み込み
    this.moon = new Moon();
    this.scene.add(this.moon);

    // 背景作成
    const geo_star  = new THREE.SphereGeometry(500, 60, 40);
    geo_star.scale(-1, 1,1);
    const mat_star  = new THREE.MeshBasicMaterial({
      map: new THREE.TextureLoader().load("{% static 'images/galaxy_starfield.jpg' %}"),
    })
    this.mesh_star  = new THREE.Mesh(geo_star, mat_star);
    this.scene.add(this.mesh_star);

    // ループ関数コール
    this.render();

    // 画面リサイズ関数コール
    window.addEventListener("resize", () => {
      this.onResize();
    });

  }

  render() {

    // 背景を右に回転
    this.mesh_star.rotation.y += 0.0006;

    // 地球回転関数コール
    this.earth.update();

    // 月回転関数コール
    this.moon.update();

    // カメラコントローラーの更新
    this.controller.update();

    // 画面に表示
    this.renderer.render(this.scene, this.camera);

    // 次のフレームコール
    requestAnimationFrame(() => { this.render(); });

  }

  onResize() {
    // サイズを取得
    const width = window.innerWidth;
    const height = window.innerHeight;

    // レンダラーのサイズを調整する
    this.renderer.setPixelRatio(window.devicePixelRatio);
    this.renderer.setSize(width, height);

    // カメラのアスペクト比を正す
    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
  }

}

