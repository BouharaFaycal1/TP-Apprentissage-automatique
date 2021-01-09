import { Component, OnInit } from '@angular/core';
import { DepannageAvignonService } from '../service/depannage-avignon.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-metiers',
  templateUrl: './metiers.component.html',
  styleUrls: ['./metiers.component.css']
})
export class MetiersComponent implements OnInit {
  metiers: any;
  //metierForm:FormGroup;
  metierForm = new FormGroup({
    libelle:  new FormControl('test'),
    image:  new FormControl(),
   });
  constructor(public serviceDepannage: DepannageAvignonService,private router:Router, private formBuilder: FormBuilder) {

    // this.metierForm = this.formBuilder.group({
     
    // });
  }

  ngOnInit(): void {
    this.serviceDepannage.getMetiers().subscribe(data => {
      this.metiers = data;
    });
  }

  redirectTo(idMetier){  
   let url = '/categories';
    this.router.navigate([url],
         {queryParams: {idMetier: idMetier.id}});
  }

  addMetier(){
console.log(this.metierForm);
this.serviceDepannage.addMetier(this.metierForm.value).subscribe(data =>{
console.log('data',data)
});
  }
  



}
