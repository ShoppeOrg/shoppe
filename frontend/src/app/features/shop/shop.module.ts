import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from 'src/app/material.module';

import { ShopRoutingModule } from './shop-routing.module';
import {ShopComponent} from './pages/shop/shop.component';
import { ShopItemComponent } from './components/shop-item/shop-item.component';

@NgModule({
  declarations: [ShopComponent, ShopItemComponent],
  imports: [MaterialModule, CommonModule, ShopRoutingModule],
  providers: []
})
export class ShopModule {}
