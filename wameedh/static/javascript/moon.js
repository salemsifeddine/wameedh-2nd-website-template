import * as THREE from 'three';


/**
 * MOON
 */
export class Moon extends THREE.Group {
  constructor() {
    super();

    {
      const geo  = new THREE.SphereGeometry(10, 60, 120);
      const mat = new THREE.MeshPhongMaterial({
        map: new THREE.TextureLoader().load("{% static 'images/moon_texture.jpg' %}"),
      })

      this.moon = new THREE.Mesh(geo, mat);
      this.moon.position.set(0,0,0);
      this.add(this.moon);

      this.r = 200;
      this.theta = 0;
      this.dTheta = 2 * Math.PI / 1000;
    }
  }

  update() {

    this.theta += this.dTheta;
    this.moon.position.x = this.r * Math.cos(this.theta);
    this.moon.position.z = this.r * Math.sin(this.theta);
  }

};