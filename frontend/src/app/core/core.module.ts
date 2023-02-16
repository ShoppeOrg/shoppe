import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


import { HeaderComponent } from './header/header.component';
import { MaterialModule } from '../material.module';
import { RouterModule } from '@angular/router';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './auth/pages/login/login.component';
import { PageHeaderComponent } from '../shared/page-header/page-header.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { LoginFormComponent } from './auth/components/login-form/login-form.component';

@NgModule({
  imports: [CommonModule, MaterialModule, RouterModule, ReactiveFormsModule, FormsModule],
  declarations: [
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    PageHeaderComponent,
    NotFoundComponent,
    LoginFormComponent
  ],
  exports: [HeaderComponent, FooterComponent, PageHeaderComponent]
})
export class CoreModule {}
