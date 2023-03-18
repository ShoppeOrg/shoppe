import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ShopItemComponent } from './components/shop-item/shop-item.component';
import { ShopComponent } from './pages/shop/shop.component';

const routes: Routes = [
  {
    path: '',
    component: ShopItemComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ShopRoutingModule {}
