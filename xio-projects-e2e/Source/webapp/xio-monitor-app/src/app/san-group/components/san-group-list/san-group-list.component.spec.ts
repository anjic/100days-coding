import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SanGroupListComponent } from './san-group-list.component';

describe('SanGroupListComponent', () => {
  let component: SanGroupListComponent;
  let fixture: ComponentFixture<SanGroupListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SanGroupListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SanGroupListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
