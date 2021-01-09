import { Component, OnInit } from '@angular/core';
import { DepannageAvignonService } from '../service/depannage-avignon.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-categorie',
  templateUrl: './categorie.component.html',
  styleUrls: ['./categorie.component.css']
})
export class CategorieComponent implements OnInit {
  categories: any;
  idMetier: any
  constructor(public serviceDepannage: DepannageAvignonService, private route: ActivatedRoute,private router:Router) {

  }

  ngOnInit(): void { 
    this.route.queryParamMap.subscribe(queryParams => {
      this.idMetier = queryParams.get("idMetier");
      if (this.idMetier !== undefined) {
        this.serviceDepannage.getCategories(this.idMetier).subscribe(data => {
          this.categories = data;
        });
      }
    });
  }

  redirectTo(categorie){  
    let url = '/prestations';
     this.router.navigate([url],
          {queryParams: {idCategorie: categorie.id}});
   }

}
