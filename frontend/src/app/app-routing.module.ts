import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/shop',
    pathMatch: 'full'
  },
  {
    path: 'shop',
    loadChildren: () => import('./features/shop/shop.module').then(m => m.ShopModule)
  },
  {
    path: 'story',
    loadChildren: () => import('./features/story/story.module').then(m => m.StoryModule)
  },
  {
    path: 'blog',
    loadChildren: () => import('./features/blog/blog.module').then(m => m.BlogModule)
  },
  {
    path: 'cart',
    loadChildren: () => import('./features/cart/cart.module').then(m => m.CartModule)
  },
  {
    path: 'my-profile',
    loadChildren: () => import('./features/user/user.module').then(m => m.UserModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
