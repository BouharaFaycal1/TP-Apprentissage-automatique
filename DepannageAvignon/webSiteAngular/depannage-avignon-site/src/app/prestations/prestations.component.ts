import { Component, OnInit } from '@angular/core';
import { DepannageAvignonService } from '../service/depannage-avignon.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-prestations',
  templateUrl: './prestations.component.html',
  styleUrls: ['./prestations.component.css']
})
export class PrestationsComponent implements OnInit {

  prestations: any;
  idCategorie: any
  constructor(public serviceDepannage: DepannageAvignonService, private route: ActivatedRoute) {

  }

  ngOnInit(): void {
    this.route.queryParamMap.subscribe(queryParams => {
      this.idCategorie = queryParams.get("idCategorie");
      if (this.idCategorie !== undefined) {
        this.serviceDepannage.getPrestation(this.idCategorie).subscribe(data => {
          this.prestations = data;
        });
      }
    });
  }

}
