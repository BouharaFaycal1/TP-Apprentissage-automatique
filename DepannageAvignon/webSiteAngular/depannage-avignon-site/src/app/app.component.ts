import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'depannage-avignon-site';

  getUrlImg(){
    return "url('http://localhost/img/bricoleur6.jpg')";
  }
}


