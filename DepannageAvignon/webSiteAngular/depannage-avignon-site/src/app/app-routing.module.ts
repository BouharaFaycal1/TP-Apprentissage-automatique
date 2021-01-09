import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MetiersComponent } from './metiers/metiers.component';
import { CategorieComponent } from './categorie/categorie.component';
import { PrestationsComponent } from './prestations/prestations.component';

const routes: Routes = [
  { path: 'metiers', component: MetiersComponent},
  { path: 'categories', component: CategorieComponent},
  { path: 'prestations', component: PrestationsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
