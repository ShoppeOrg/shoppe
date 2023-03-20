import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ShopComponent } from './pages/shop/shop.component';
import {ShopDetailsComponent} from './pages/shop-details/shop-details.component';

const routes: Routes = [
  {
    path: '',
    component: ShopComponent
  },
  {
    path: ':id',
    component:ShopDetailsComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ShopRoutingModule {}
