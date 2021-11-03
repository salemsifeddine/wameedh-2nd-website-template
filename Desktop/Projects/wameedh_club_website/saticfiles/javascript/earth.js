import * as THREE from 'three';


/**
 * EARTH
 */
export class Earth extends THREE.Group {
  constructor() {
    super();

    /**
     * GROUND
     */
    {
      const geo  = new THREE.SphereGeometry(100, 60, 60);
      const mat = new THREE.MeshPhongMaterial({
        map: new THREE.TextureLoader().load("{% static './images/earthmap1k.jpg' %}"),
        bumpMap: new THREE.TextureLoader().load("{% static 'images/earthbump1k.jpg' %}"),
        bumpScale: 2.5,
        specularMap: new THREE.TextureLoader().load("{% static 'images/earthspec1k.jpg' %}"),
      })

      this.ground = new THREE.Mesh(geo, mat);
      this.ground.receiveShadow = true;
      this.add(this.ground);
    }

    /**
     * CLOUD
     */
    {
      const geo = new THREE.SphereGeometry(103, 60, 60);
      const mat = new THREE.MeshPhongMaterial({
        map: new THREE.TextureLoader().load("{% static 'images/earthcloud.jpg' %}"),
        transparent: true,
        blending: THREE.AdditiveBlending,
      });

      this.cloud = new THREE.Mesh(geo, mat);
      this.cloud.castShadow = true;
      this.add(this.cloud);
    }
  }

  update() {
    this.ground.rotation.y += 0.0006;
    this.cloud.rotation.y += 0.0008;
  }

};