import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MetiersComponent } from './metiers/metiers.component';
import { HttpClientModule } from '@angular/common/http';
import { DepannageAvignonService } from './service/depannage-avignon.service';
import { CategorieComponent } from './categorie/categorie.component';
import { PrestationsComponent } from './prestations/prestations.component';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    MetiersComponent,
    CategorieComponent,
    PrestationsComponent,
   
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ReactiveFormsModule
  ],
  providers: [DepannageAvignonService,FormBuilder],
  bootstrap: [AppComponent]
})
export class AppModule { }
