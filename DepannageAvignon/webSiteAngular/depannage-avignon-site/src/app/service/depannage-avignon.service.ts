import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
@Injectable()
export class DepannageAvignonService {
  urlMetiers = 'http://localhost/depannage-avignon/getMetier.php';
  urlCategories = 'http://localhost/depannage-avignon/getCategorie.php?idMetier=';
  urlPrestation='http://localhost/depannage-avignon/getPrestation.php?idCategorie='
  constructor(private http: HttpClient) { 
  }

  getMetiers(){
    return this.http.get(this.urlMetiers);
  }

  getCategories(idMetier){
    return this.http.get(this.urlCategories+idMetier);
  }

  getPrestation(idCategorie){
    return this.http.get(this.urlPrestation+idCategorie);
  }

  addMetier(metier:any){
    const headers = { 'Authorization': 'Bearer my-token', 'My-Custom-Header': 'foobar' };
    const body = { libelle: metier.libelle };
   return this.http.post<any>('http://localhost/depannage-avignon/addMetier.php', body,{ headers }); 
  }
}
